from .models import Cart, Custumer



from django.views.generic import View




class CartMixin(View):

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            customer = Custumer.objects.filter(user=request.user).first()
            if not customer:
                customer = Custumer.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)

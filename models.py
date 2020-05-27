from django.db import models

# Create your models here.


class Customer(models.Model):
    objects = None
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=False)
    note = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + ' ==== có số điện thoại: ' + str(self.phone) + ' ==== và địa chỉ là: ' + str(self.address)

class Order(models.Model):
    CATEGORY = (
        ('Dịch thuật', 'Dịch thuật'),
        ('Công chứng', 'Công chứng'),
        ('Sao y', 'Sao y'),
        ('Dịch vụ Visa', 'Dịch vụ visa'),
    )
    STATUS = (
        ('Đợi xác nhận', 'Đợi xác nhận'),
        ('Đang làm', 'Đang làm'),
        ('Đã gửi khách', 'Đã gửi khách'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order_name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True, default=50000)
    fee = models.IntegerField(null=True, default=20000)
    deposit = models.IntegerField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY,default='Dịch thuật')
    status = models.CharField(max_length=200, null=True, choices=STATUS,default='Đang làm')
    payment_status = models.BooleanField(default=False)
    note = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return 'ID khách hàng: ' + str(self.customer_id) + '  => Tên khách hàng: =  ' + self.customer.name + '  => Dịch vụ : ' + self.order_name + '==== Giá tiền là: ' + str(self.price) + '==== với số lượng là: ' + str(self.quantity)

    def sum(self):
        return self.price * self.quantity + self.fee

    def phaithu(self):
        return self.price * self.quantity +self.fee - self.deposit

class OrderFee(models.Model):
    CATEGORY = (
        ('Chi công chứng', 'Chi công chứng'),
        ('Chi ship', 'Chi ship'),
        ('Chi cộng tác viên', 'Chi cộng tác viên'),
        ('Chi cố định', 'Chi cố định'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    fee_name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY,default='Chi ship')
    fee = models.IntegerField(null=True,default=20000)
    note = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    payment_status = models.BooleanField(default=False)
    def __str__(self):
        return 'ID đơn hàng : ' + str(self.order_id) + '  ==== Tên phiếu chi:  ' + str(self.fee_name) + '==== Số tiền chi là: ' + str(self.fee) + '==== Loại chi: ' + str(self.category)

    def tongphi(self):
        return self.fee

    def loinhuan(self):
        return self.order.price * self.order.quantity + self.order.fee - self.fee


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .filters import OrderFilter
from django.db.models import Sum,Min,Max, Avg

# Create your views here.

def home(request):
	orders = Order.objects.all().order_by('-date_created')
	customers = Customer.objects.all().order_by('-date_created')
	chiphi = OrderFee.objects.all().order_by('-date_created')


	total_customers = customers.count()
	total_orders = orders.count()

	paid = orders.filter(payment_status = 'True').count()
	unpaid = orders.filter(payment_status = 'False').count()

	order_paid = orders.filter(payment_status = 'True')
	order_unpaid = orders.filter(payment_status = 'False')

	slg_xacnhan = orders.filter(status = 'Đợi xác nhận').count()
	slg_danglam = orders.filter(status = 'Đang làm').count()
	slg_daguikhach = orders.filter(status = 'Đã gửi khách').count()

	order_xacnhan = orders.filter(status = 'Đợi xác nhận')
	order_danglam = orders.filter(status = 'Đang làm')
	order_daguikhach = orders.filter(status = 'Đã gửi khách')

	month_order = orders.filter(date_created__month = '05')

	tongdt=0
	for b in orders:
		c = b.price * b.quantity + b.fee
		tongdt+=c

	tongthu = 0
	for b in order_paid:
		c = b.price * b.quantity + b.fee
		tongthu+=c

	chuathu = 0
	for b in order_unpaid:
		c = b.price * b.quantity +b.fee - b.deposit
		chuathu+=c

	phaithu = 0
	for b in order_unpaid:
		c = b.price * b.quantity +b.fee - b.deposit
		phaithu+=c

	datcoc = 0
	for b in order_paid:
		c = b.deposit
		datcoc+=c

	phuphi = 0
	for b in orders:
		c = b.fee
		phuphi+=c

	chi = 0
	for b in chiphi:
		c = b.fee
		chi += c



	context = {'orders': orders,'customers': customers,'chiphi':chiphi,
			   'total_orders':total_orders, 'total_customers':total_customers,
			   'paid':paid,'unpaid':unpaid,
			   'tongdt':tongdt,'tongthu':tongthu,'chuathu':chuathu,'phaithu':phaithu,'datcoc':datcoc,'phuphi':phuphi,'chi':chi,
			   'month_order':month_order,
			   }
	return render(request, 'don_hang/dashboard.html',context)

def khach_hang(request,id,id2):
	kh = Customer.objects.get(pk=id)
	dh = kh.order_set.get(pk=id2)
	cp = dh.orderfee_set.all()
	request.session['cp'] = cp

	e = dh.quantity * dh.price

	d = 0
	for a in cp:
		d+=a.fee

	f = e-d




	context = {'kh':kh,'dh':dh,'cp':cp,'d':d,'e':e,'f':f,
			   # 'orders': orders, 'customers': customers, 'chiphi': chiphi,
			   }
	return render(request, 'don_hang/kh.html',context)

# def don_hang(request,id):
# 	dh = Order.objects.get(pk=id)
# 	cp = dh.orderfee_set.all()
#
# 	context = {'dh':dh,'cp':cp,}
# 	return render(request, 'don_hang/dh.html',context)

from django.db import models
from django.utils.datetime_safe import datetime
from django.contrib.auth import get_user_model
from ..settings.models import *
from ..base.models import UserModel
from django.db.models.signals import post_save

Users = get_user_model()


class Amenities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    address2 = models.CharField(max_length=225, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    postal_code = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    region = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    unit_qty = models.DecimalField(max_digits=2, decimal_places=0)
    amenities = models.BooleanField(blank=True, null=True)
    type_resource = models.ForeignKey(Classification, blank=True, null=True, on_delete=models.CASCADE)
    supplier = models.ManyToManyField(Supplier, blank=True, null=True)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Building'
        verbose_name_plural = 'Buildings'
        ordering = ['create_to']

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)


def remove_relational_supplier(sender, instance, **kwargs):
    if instance.state is False:
        supplier = instance.id
        building = Building.objects.filter(supplier=supplier)
        for rec in building:
            rec.supplier.remove(supplier)


post_save.connect(remove_relational_supplier, sender=Supplier)


def remove_relational_resources(sender, instance, **kwargs):
    if instance.state is False:
        classification = instance.id
        building = Building.objects.filter(type_resource=classification)
        for rec in building:
            rec.type_resource.remove(classification)


post_save.connect(remove_relational_resources, sender=Classification)


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.DecimalField(max_digits=2, decimal_places=0)
    meter_qty = models.DecimalField(max_digits=2, decimal_places=0, blank=True,
                                    null=True)
    flat = models.CharField(max_length=20)
    expiration_date = models.DateField(blank=True, null=True)
    init_date = models.DateField(blank=True, null=True)
    renovation_date = models.DateField(blank=True, null=True)
    rent_price = models.IntegerField(default=0)
    renter = models.ForeignKey(Users, blank=True, null=True,
                               on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    type_resource = models.ForeignKey(Classification, blank=True, null=True,
                                      on_delete=models.CASCADE)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    garage = models.BooleanField(default=False)
    state = models.BooleanField(default=True)

    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ['create_to']

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name)

    def save(self, *args, **kwargs):
        if self.number != 0 and self.flat != None:
            if self.number < 10:
                apartment = f'{self.flat}0{self.number}'
            else:
                apartment = f'{self.flat}{self.number}'
            self.name = apartment
        super(Unit, self).save(*args, **kwargs)


def remove_relational_building(sender, instance, **kwargs):
    if instance.state is False:
        building = instance.id
        unit = Unit.objects.filter(building_id=building)
        for rec in unit:
            rec.building_id.remove(building)


post_save.connect(remove_relational_building, sender=Building)


def remove_relational_resources_unit(sender, instance, **kwargs):
    if instance.state is False:
        classification = instance.id
        unit = Unit.objects.filter(type_resource=classification)
        for rec in unit:
            rec.type_resource.remove(classification)


post_save.connect(remove_relational_resources_unit, sender=Classification)


class CommonExpenses(models.Model):
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    payment_date = models.DateField()
    total_amount = models.PositiveIntegerField(default=1)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    # create_by = models.ForeignKey(Users, blank=True, null=True, related_name='author_post', on_delete=models.CASCADE)
    # update_by = models.ForeignKey(Users, blank=True, null=True, related_name='post_update', on_delete=models.CASCADE)

    def __str__(self):
        date = self.payment_date.strftime('%m/%Y')
        return f'{self.building}-{date}'

    class Meta:
        verbose_name_plural = 'Common Expenses'
        ordering = ['payment_date']


def remove_relational_building_ce(sender, instance, **kwargs):
    if instance.state is False:
        building = instance.id
        commonExpenses = CommonExpenses.objects.filter(building=building)
        for rec in commonExpenses:
            rec.building.remove(building)


post_save.connect(remove_relational_building_ce, sender=Building)


class CommonExpensesLines(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.PositiveIntegerField(default=1)
    concept = models.ForeignKey(Services, on_delete=models.CASCADE)
    common_expenses = models.ForeignKey(CommonExpenses, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Common Expenses Lines'
        ordering = ['create_to']


#
def remove_relational_services(sender, instance, **kwargs):
    if instance.state is False:
        services = instance.id
        commonExpensesLines = CommonExpensesLines.objects.filter(concept=services)
        for rec in commonExpensesLines:
            rec.concept.remove(services)


post_save.connect(remove_relational_services, sender=Services)


def remove_relational_common_expenses(sender, instance, **kwargs):
    if instance.state is False:
        commonExpenses = instance.id
        commonExpensesLines = CommonExpensesLines.objects.filter(common_expenses=commonExpenses)
        for rec in commonExpensesLines:
            rec.common_expenses.remove(commonExpenses)


post_save.connect(remove_relational_common_expenses, sender=CommonExpenses)


class Garage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    payment_date = models.DateField(blank=True, null=True)
    state = models.BooleanField(default=True)
    total_amount = models.IntegerField(default=1)

    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Garage'
        verbose_name_plural = 'Garages'
        ordering = ['create_to']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        date = self.payment_date.strftime('%m/%Y')
        self.name = f'{self.building}-{date}'
        super(Garage, self).save(*args, **kwargs)


def remove_relational_building_garage(sender, instance, **kwargs):
    if instance.state is False:
        building = instance.id
        garage = Garage.objects.filter(building=building)
        for rec in garage:
            rec.building.remove(building)


post_save.connect(remove_relational_building_garage, sender=Building)


class GarageLines(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(default=1)
    apartment = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    voucher = models.ImageField(upload_to='images/voucher/', blank=True, null=True)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)

    state = models.BooleanField(default=True)
    create_to = models.DateTimeField(auto_now_add=True)
    update_to = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Garage Line'
        verbose_name_plural = 'Garages Lines'
        ordering = ['create_to']

    def __str__(self):
        month = self.create_to.strftime('%m')
        return f'{self.apartment}-{month}'


def remove_relational_garage(sender, instance, **kwargs):
    if instance.state is False:
        garage_id = instance.id
        lines = GarageLines.objects.filter(garage=garage_id)
        for rec in lines:
            rec.garage.remove(garage_id)


post_save.connect(remove_relational_garage, sender=Garage)


def remove_relational_apartment(sender, instance, **kwargs):
    if instance.state is False:
        apartment_id = instance.id
        lines = GarageLines.objects.filter(apartment=apartment_id)
        for rec in lines:
            rec.apartment.remove(apartment_id)


post_save.connect(remove_relational_garage, sender=Unit)

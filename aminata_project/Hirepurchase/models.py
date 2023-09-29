from django.db import models

class HirePurchase(models.Model):
    # equipment_name = models.ForeignKey(Catalog,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    installment_period = models.IntegerField() 
    date = models.DateField(auto_now_add=True)
    payment_frequency = models.CharField(
        max_length=20,
        choices=[('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('annually', 'Annually'), ('semi_annually', 'Semi-Annually')]
    )

    def calculate_installment_and_balance(self):
        if self.payment_frequency == 'monthly':
            installment_amount = (self.total_price - self.down_payment) / self.installment_period
            self.remaining_balance = self.total_price - self.down_payment
        elif self.payment_frequency == 'quarterly':
            installment_amount = (self.total_price - self.down_payment) / (self.installment_period / 3)
            self.remaining_balance = self.total_price - self.down_payment
        elif self.payment_frequency == 'annually':
            installment_amount = (self.total_price - self.down_payment) / (self.installment_period / 2)
            self.remaining_balance = self.total_price - self.down_payment
        elif self.payment_frequency == 'semi_annually':
            installment_amount = (self.total_price - self.down_payment) / self.installment_period 
            self.remaining_balance = self.total_price - self.down_payment
        else:
            installment_amount = 0
            self.remaining_balance = 0

        return installment_amount

    def save(self, *args, **kwargs):
        installment_amount = self.calculate_installment_and_balance()
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.equipment_name

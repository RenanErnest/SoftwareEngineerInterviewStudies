package Visitor.Visitors;

import Visitor.PaymentMethods.CreditCardPayment;
import Visitor.PaymentMethods.DebitCardPayment;
import Visitor.PaymentMethods.DigitalWalletPayment;

public interface Visitor{
    Object visitCreditCardPayment(CreditCardPayment payment);
    Object visitDebitCardPayment(DebitCardPayment payment);
    Object visitDigitalWalletPayment(DigitalWalletPayment payment);
}


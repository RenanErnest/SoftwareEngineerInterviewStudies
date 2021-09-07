package Visitor.Visitors;

import java.util.ArrayList;

import Visitor.PaymentMethods.CreditCardPayment;
import Visitor.PaymentMethods.DebitCardPayment;
import Visitor.PaymentMethods.DigitalWalletPayment;

public class GetPaymentPartnersVisitor implements Visitor{

    @Override
    public Object visitCreditCardPayment(CreditCardPayment payment) {
        return payment.partnersAllowList;
    }

    @Override
    public Object visitDebitCardPayment(DebitCardPayment payment) {
        return payment.partnersAllowList;
        
    }

    @Override
    public Object visitDigitalWalletPayment(DigitalWalletPayment payment) {
        return new ArrayList<String>();
    }
    
}

package Visitor;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.ArrayList;

import Visitor.PaymentMethods.CreditCardPayment;
import Visitor.PaymentMethods.DebitCardPayment;
import Visitor.PaymentMethods.DigitalWalletPayment;
import Visitor.PaymentMethods.Payment;
import Visitor.Visitors.Visitor;
import Visitor.Visitors.GetPaymentPartnersVisitor;

public class Application {
    public static void main(String[] args) {
        List<Payment> paymentMethods = new ArrayList<Payment>(Arrays.asList(new CreditCardPayment(), 
                                                                            new DebitCardPayment(), 
                                                                            new DigitalWalletPayment()));

        Set<String> paymentPartners = new HashSet<String>();

        Visitor getPaymentPartnersVisitor = new GetPaymentPartnersVisitor();

        for(Payment paymentMethod : paymentMethods) {
            paymentPartners.addAll((List<String>) paymentMethod.accept(getPaymentPartnersVisitor));
        }

        System.out.println(paymentPartners);
    }
}

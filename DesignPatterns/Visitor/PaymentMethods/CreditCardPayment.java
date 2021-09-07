package Visitor.PaymentMethods;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import Visitor.Visitors.Visitor;

public class CreditCardPayment implements Payment {
    public List<String> partnersAllowList = new ArrayList<String>(Arrays.asList("Mastercard", "Visa"));
    List<Integer> paymentInInstallmentsOptions = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12));

    @Override
    public void process() {
        // do some process
    }

    @Override
    public Object accept(Visitor v) {
        return v.visitCreditCardPayment(this);
    }
}

package Visitor.PaymentMethods;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import Visitor.Visitors.Visitor;

public class DebitCardPayment implements Payment {
    public List<String> partnersAllowList = new ArrayList<String>(Arrays.asList("Mastercard", "Visa", "American Express"));

    @Override
    public void process() {
        // do some process
    }

    @Override
    public Object accept(Visitor v) {
        return v.visitDebitCardPayment(this);
    }
}

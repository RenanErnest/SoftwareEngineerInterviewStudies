package Visitor.PaymentMethods;

import Visitor.Visitors.Visitor;

public class DigitalWalletPayment implements Payment {
    
    public int getUserBalance(){
        return 30;
    }

    @Override
    public void process() {
        // do some process
    }

    @Override
    public Object accept(Visitor v) {
        return v.visitDigitalWalletPayment(this);
    }
}

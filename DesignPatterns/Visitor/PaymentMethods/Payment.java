package Visitor.PaymentMethods;

import Visitor.Visitors.Visitor;

public interface Payment {
    void process();
    Object accept(Visitor v);
}

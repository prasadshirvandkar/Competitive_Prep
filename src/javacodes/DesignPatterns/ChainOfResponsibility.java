package javacodes.DesignPatterns;

import java.util.*;

class Chain<T> {
    ChainProcessor<T> processor;

    Chain() {
        processor = new C1Cache<T>(new C2Cache<T>(new C3Cache<T>(null)));
    }

    public void process(T request) {
        processor.process(request);
    }
}

abstract class ChainProcessor<T> {
    protected List<T> c1 = new ArrayList<>();
    protected List<T> c2 = new ArrayList<>();
    protected List<T> c3 = new ArrayList<>();
    private ChainProcessor<T> chainProcessor;

    ChainProcessor(ChainProcessor<T> chainProcessor) {
        this.chainProcessor = chainProcessor;
    }

    public void process(T request) {
        if(request != null) {
            chainProcessor.process(request);
        }
    }
}

class C1Cache<T> extends ChainProcessor<T> {
    C1Cache(ChainProcessor<T> c1Cache) {
        super(c1Cache);
    }

    @Override
    public void process(T request) {
        if(c1.size() != 2) {
            c1.add(request);
            System.out.println("Added Object to C1 Cache");
        } else {
            super.process(request);
        }
    }
}

class C2Cache<T> extends ChainProcessor<T> {
    C2Cache(ChainProcessor<T> c2Cache) {
        super(c2Cache);
    }

    @Override
    public void process(T request) {
        if(c2.size() != 2) {
            c2.add(request);
            System.out.println("C1 Full. Added Object to C2 Cache");
        } else {
            super.process(request);
        }
    }
}

class C3Cache<T> extends ChainProcessor<T> {
    C3Cache(ChainProcessor<T> c3Cache) {
        super(c3Cache);
    }

    @Override
    public void process(T request) {
        if(c3.size() != 2) {
            c3.add(request);
            System.out.println("C3 Full. Added to C3 Cache");
        } else {
            System.out.println("Cache Memory is Full");
            return;
        }
    }
}

public class ChainOfResponsibility {
    public static void main(String[] args) {
        Chain<Integer> chainProcessor = new Chain<>();
        for(int i=1; i<=10; i++) {
            chainProcessor.process(i*10);
        }

    }
}
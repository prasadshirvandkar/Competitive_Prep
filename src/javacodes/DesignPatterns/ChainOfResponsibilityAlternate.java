package javacodes.DesignPatterns;

import java.util.*;

interface CacheChain<T> {
    void setNextChain(CacheChain<T> cacheChain);
    void processRequest(T request);
}

abstract class CacheList<T> {
    protected List<T> c1 = new ArrayList<>();
    protected List<T> c2 = new ArrayList<>();
    protected List<T> c3 = new ArrayList<>();
}

class C1CacheAlt<T> extends CacheList<T> implements CacheChain<T> {
    CacheChain<T> nextChain;

    @Override
    public void setNextChain(CacheChain<T> nextChain) {
        this.nextChain = nextChain;
    }

    @Override
    public void processRequest(T request) {
        if(c1.size() != 2) {
            c1.add(request);
            System.out.println("Added Object to C1 Cache");
        } else {
            nextChain.processRequest(request);
        }
    }
}

class C2CacheAlt<T> extends CacheList<T> implements CacheChain<T> {
    CacheChain<T> nextChain;

    @Override
    public void setNextChain(CacheChain<T> nextChain) {
        this.nextChain = nextChain;
    }

    @Override
    public void processRequest(T request) {
        if(c2.size() != 2) {
            c2.add(request);
            System.out.println("Added Object to C2 Cache");
        } else {
            nextChain.processRequest(request);
        }
    }
}

class C3CacheAlt<T> extends CacheList<T> implements CacheChain<T> {
    CacheChain<T> nextChain;

    @Override
    public void setNextChain(CacheChain<T> nextChain) {
        this.nextChain = nextChain;
    }

    @Override
    public void processRequest(T request) {
        if(c3.size() != 2) {
            c3.add(request);
            System.out.println("Added Object to C3 Cache");
        } else {
            System.out.println("Cache is FULL");
        }
    }
}

class ChainProcessorAlternate<T> {
    CacheChain<T> chain;
    ChainProcessorAlternate() {
        chain = new C1CacheAlt<T>();
        CacheChain<T> c2 = new C2CacheAlt<T>();
        CacheChain<T> c3 = new C3CacheAlt<T>();
        chain.setNextChain(c2);
        c2.setNextChain(c3);
    }

    public void processRequest(T request) {
        chain.processRequest(request);
    }
}

public class ChainOfResponsibilityAlternate {
    public static void main(String[] args) {
        ChainProcessorAlternate<Integer> chainProcessorAlternate  = new ChainProcessorAlternate<>();

        for(int i=0; i<10; i++) {
            chainProcessorAlternate.processRequest(i*10);
        }
    }
}
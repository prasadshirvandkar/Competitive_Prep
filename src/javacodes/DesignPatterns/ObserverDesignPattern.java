package javacodes.DesignPatterns;

import java.util.*;

interface Observable {
    public void registerObserver(Observer o);
    public void removeObserver(Observer o);
    public void notifyObservers();
}

interface Observer {
    void update(int price);
}

class StockData implements Observable {
    List<Observer> list = new ArrayList<>();
    int stockPrice = 100;

    @Override
    public void registerObserver(Observer observer) {
        list.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        list.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for(Observer o: list) {
            o.update(stockPrice);
        }
    }

    public void setStockPrice(int stockPrice) {
        this.stockPrice = stockPrice;
        notifyObservers();
    }
}

class StockPriceObserver implements Observer {
    @Override
    public void update(int price) {
        System.out.println("Stock Price Updated: $"+price);
    }
}

class StockMetaData implements Observer {
    int high = 100;
    int low = 100;
    int changedFromDay = 0;
    int percentageIncrease = 0;

    @Override
    public void update(int price) {
        low = Math.min(price, low);
        high = Math.max(price, high);
        changedFromDay = price - 100;
        percentageIncrease = (changedFromDay / 100) * 100;
        System.out.println("Stock Price Updated: \nLow: "+low+"\nHigh: "+high
                    +"\nChanged By: "+changedFromDay+"\nPercentage Increased: "+percentageIncrease+"%");
    }

}

public class ObserverDesignPattern {
    public static void main(String[] args) throws InterruptedException {
        StockPriceObserver stockPriceObserver = new StockPriceObserver();
        StockMetaData stockMetaData = new StockMetaData();

        StockData stockData = new StockData();
        stockData.registerObserver(stockPriceObserver);
        stockData.registerObserver(stockMetaData);

        Thread.sleep(1400);
        stockData.setStockPrice(140);
        System.out.println();
        Thread.sleep(1400);
        stockData.setStockPrice(120);
        System.out.println();
        Thread.sleep(1400);
        stockData.setStockPrice(90);
        System.out.println();
        Thread.sleep(1400);
        stockData.setStockPrice(110);
        System.out.println();
        Thread.sleep(1400);
        stockData.setStockPrice(50);
        System.out.println();

    }
}
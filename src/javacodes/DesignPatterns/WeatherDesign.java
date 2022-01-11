package javacodes.DesignPatterns;

import java.util.ArrayList;
import java.util.List;

interface WeatherObservable {
    void registerObserver();
    void unregisterObserver();
    void notifyObserver();
}

interface WeatherObserver {
    void getDataAndUpdate();
}

class WeatherService implements WeatherObservable {
    List<WeatherObserver> observers = new ArrayList<>();

    @Override
    public void registerObserver() {
    }

    @Override
    public void unregisterObserver() {
    }

    @Override
    public void notifyObserver() {
    }

    
}

public class WeatherDesign {
    
}
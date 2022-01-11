package javacodes.CustomImplementations;

import java.util.HashMap;
import java.util.Map;

class CacheEntry<K, V> {
    K key;
    V value;
    CacheEntry<K, V> prev;
    CacheEntry<K, V> next;

    CacheEntry(K key, V value, CacheEntry<K, V> prev, CacheEntry<K, V> next) {
        this.key = key;
        this.value = value;
        this.prev = prev;
        this.next = next;
    }
}

interface Cache<K, V> {
    void put(K key, V value);
    V get(K key);
}

class LRUCache<K, V> implements Cache<K, V> {
    Map<K, CacheEntry<K, V>> cacheMap = new HashMap<>();
    CacheEntry<K, V> start = null, end = null;
    final int CACHE_SIZE = 4;

    @Override
    public void put(K key, V value) {
        CacheEntry<K, V> cacheEntry = cacheMap.get(key);
        if(cacheEntry != null) {
            cacheEntry.value = value;
            remove(cacheEntry);
            addToTop(cacheEntry);
        } else {
            CacheEntry<K, V> newCacheEntry = new CacheEntry<>(key, value, null, null);
            if(cacheMap.size() >= CACHE_SIZE) {
                cacheMap.remove(start.key);
                remove(start);
                addToTop(newCacheEntry);
            } else {
                if(start == null && end == null) {
                    start = newCacheEntry;
                    end = newCacheEntry;
                } else {
                    addToTop(newCacheEntry);
                }
            }
            cacheMap.put(key, newCacheEntry);
        }
        print();
    }

    private void addToTop(CacheEntry<K, V> cacheEntry) {
        end.next = cacheEntry;
        cacheEntry.prev = end;
        end = cacheEntry;
    }

    private void remove(CacheEntry<K, V> cacheEntry) {
        if(cacheEntry.prev != null) {
            cacheEntry.prev.next = cacheEntry.next;
        } else {
            start = cacheEntry.next;
        }

        if(cacheEntry.next != null) {
            cacheEntry.next.prev = cacheEntry.prev;
        } else {
            end = cacheEntry.prev;
        }
    }

    @Override
    public V get(K key) {
        CacheEntry<K, V> cacheEntry = cacheMap.get(key);
        if(cacheEntry != null) {
            remove(cacheEntry);
            addToTop(cacheEntry);
            return cacheEntry.value;
        }
        return null;
    }

    public void print() {
        for(Map.Entry<K, CacheEntry<K,V>> entry: cacheMap.entrySet()) {
            System.out.print(entry.getKey()+" -> "+entry.getValue().value+" | ");
        }
        System.out.println();
    }
}

public class CustomLRUCache {
    public static void main(String[] args) {
        Cache<Integer, Integer> lruCache = new LRUCache<>();
        lruCache.put(10, 10);
        lruCache.put(20, 20);
        lruCache.put(30, 30);
        lruCache.put(40, 40);

        lruCache.put(50, 50);
        lruCache.put(20, 25);

        lruCache.get(20);
        lruCache.put(60, 60);
    }
}
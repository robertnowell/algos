package notJava;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.TreeMap;
import java.util.concurrent.ConcurrentHashMap;

/**
 * 	Followup questions:
	If a Rankable's rank is defined as it's last access time, the retain-best cache becomes an LRU cache.
	If the candidate doesn't know the 'standard' map + list LRU solution, ask them to re-implement the retain-best cache to take advantage of knowing what
	the Rank function is
	If the candidate does know the standard LRU solution, ask them to contrast the performance of their retain-best cache to the standard LRU
	(Hardmode) How would you need to enhance your solution to handle Rankables that frequently changed Rank?
	LRU is the first step of this - Objects increase in rank each time they are accessed. Another variant might be Most/Least Frequently Used, where rank
	increases or decreases by one each access
	If you had a cache of a graph that traversals were happening on, you could declare a rank based on where the traversal was at the moment, and so
	ranks could change without being accessed (rank would be a function of how close to the traversal front the node was). In the worst case, this could
	trigger a full re-rank of the cache on each cache miss.	
 */
interface Rankable {
	/**
	* Returns the Rank of this object, using some algorithm and potentially
	
	5/23/2019 Retain-Best Cache - Unite - LinkedIn Corporate Wiki
	
	https://iwww.corp.linkedin.com/wiki/cf/display/Unite/Retain-Best+Cache 2/11
	To begin with, assume that ranks will not change once read. Don't offer this information until the candidate asks.

	Sample TreeMap Solution:
	* the internal state of the Rankable.
	*/
	long getRank();
}

interface DataSource<K, T extends Rankable> {
	T get (K key);
}

//public class RetainBestCache<K, T extends Rankable> {
//	TreeMap<K, T> map;
//	int size;
//	int maxSize;
//	K minKey;
//	T minVal;
//	DataSource data;
//
//	// Add any fields you need here
//	/* Constructor with a data source (assumed to be slow) and a cache size */
//	public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
//		this.map = new TreeMap<K, T>();
//		this.size = 0;
//		this.maxSize = entriesToRetain;
//		this.data = ds;
//	}
//	private K getMinFromMap() {
//		return null;
//	}
//	/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
//	* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
//	* evicting the T with lowest rank among the ones that it has available
//	* If there is a tie, the cache may choose any T with lowest rank to evict.
//	*/
//	public T get(K key) {
//		T val = map.get(key);
//		if (val == null) {
//			val = (T) this.data.get(key);
//			if (this.size < this.maxSize) {
//				map.put(key, val);
//				if (this.minKey == null) {
//					this.minKey = key;
//					this.minVal = val;
//				}
//				this.size++;
//			} else {
//				if (this.minVal.getRank() < val.getRank()) {
//					this.map.remove(minKey);
//					this.minKey = this.getMinFromMap();
//					this.minVal = this.map.get(this.minKey);
//					this.map.put(key, val);
//				}
//			}
//		} else {
//			return val;
//		}
//	}
//}


/**
 * basically use 
 * 	concurrent map to keep track of all elements and efficiently retrieve from cache
 * 	tree map to efficiently keep track of which element to remove when we exceed size
 * 
 * get
 * 	return if exists in cache
 * 	else 
 * 		get from datastore
 * 		put into cache
 * 		return
 *
 *put
 *	add to map
 *	add to rankmap (rank to set of keys)
 *
 *	if map exceeds size
 *		get lowest key from rankmap
 *			remove from	rankmap
 * 			remove from map
 * 
 */
//public class RetainBestCache<K, T extends Rankable> {
//	DataSource dataSource;
//	int maxNumItems;
//	ConcurrentHashMap<K, T> items;
//	TreeMap<Long, Set<K>> rankMap;
//	
//
//	// Add any fields you need here
//	/* Constructor with a data source (assumed to be slow) and a cache size */
//	public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
//		dataSource = ds;
//		maxNumItems = entriesToRetain;
//		items = new ConcurrentHashMap<K, T>();
//		rankMap = new TreeMap<Long, Set<K>>();
//	}
//
//	/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
//	* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
//	* evicting the T with lowest rank among the ones that it has available
//	* If there is a tie, the cache may choose any T with lowest rank to evict.
//	*/
//	public T get(K key) {
//		T item = items.get(key);
//
//		if (item == null) {
//			item = (T) dataSource.get(key);
//			put(key, item);
//		}
//		return item;
//	}
//	
//	private synchronized void put(K key, T item) {
//		items.put(key, item);
//		addToRankMap(item.getRank(), key);
//		if (items.size() > maxNumItems) {
//			Map.Entry<Long, Set<K>> lowestRankedEntry = rankMap.firstEntry();
//			Set<K> lowestRankedSet = lowestRankedEntry.getValue();
//			
//			K keyToDelete = lowestRankedSet.iterator().next();
//			items.remove(keyToDelete);
//			if (lowestRankedSet.size() > 1) {
//				lowestRankedSet.remove(keyToDelete);
//			} else {
//				rankMap.remove(lowestRankedEntry.getKey());
//			}
//		}
//	}
//	
//	private void addToRankMap(Long rank, K key) {
//		Set<K> set = rankMap.get(rank);
//		if (set == null) {
//			set = new HashSet<K>();
//			rankMap.put(rank, set);
//		}
//		set.add(key);
//	}
//}

public class RetainBestCache<K, T extends Rankable> {
	DataSource ds;
	PriorityQueue<Node> pq = new PriorityQueue<Node>();
	Map<K, T> map = new HashMap<K, T>();
	int maxSize;

// Add any fields you need here
/* Constructor with a data source (assumed to be slow) and a cache size */
public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
	this.ds = ds;
	this.maxSize = entriesToRetain;
}

/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
* evicting the T with lowest rank among the ones that it has available
* If there is a tie, the cache may choose any T with lowest rank to evict.
*/
public synchronized T get(K key) {
	if (map.containsKey(key)) {
		return map.get(key);
	}
	else {
		T item = (T) ds.get(key);
		map.put(key, item);
		Node<K, T> n = new Node<K, T>(key, item);
		pq.offer(n);
		
		if (pq.size() > maxSize) {
			map.remove(pq.poll().key);
		}
		return item;
	}
}

private class Node<K, T extends Rankable> implements Comparable{
	public K key;
	public T val;

	public Node(K k, T v) {
		key = k;
		val = v;
	}

	@Override
	public int compareTo(Object o) {
		Long diff = val.getRank() - ((Node) o).val.getRank();
		if (diff < 0) {
			return 1;
		} else if (diff > 0) {
			return -1;
		} else {
			return 0;
		}
	}
}
}

/**
 * lru
 * 	size
 * 	map
 * 	doublylinkedlist
 * 	datasource
 * 
 * get
 *	if elem in map,
 *		set elem-prev to elem-next and elem-next-prev to elem-prev. Append elem to end of list
 *	else:
 *		get elem from datastore
 *		add elem to end of list
 *		pop from front of list
 */

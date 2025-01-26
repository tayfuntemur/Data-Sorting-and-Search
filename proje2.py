import random

class LargeDataSortingSystem:
    def __init__(self, data):
        self.data = data

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self):
        if hasattr(self, 'sorted_data'):
            return self.sorted_data
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
       
        self.sorted_data = arr
        return arr
# Counting Sort ana fonksiyonu
    def counting_sort(self):
        arr=self.data.copy()
        max_val = max(arr)  # Dizideki en büyük değeri bul
        count = [0] * (max_val + 1)  # Sayma dizisi oluştur
        # Her elemanın kaç kez tekrarlandığını say
        for num in arr:
            count[num] += 1
        # Sayma dizisini kullanarak sıralı dizi oluştur
        sorted_arr = []
        for i in range(len(count)):
            sorted_arr.extend([i] * count[i])  # Her elemanı tekrar sayısı kadar ekle
        return sorted_arr

    def interpolation_search(self, x):
        arr = self.heap_sort()  
        low = 0
        high = len(arr) - 1
        
        while low <= high and arr[low] <= x <= arr[high]:
            if arr[high] == arr[low]:
                pos = low
            else:
                pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
            
            if arr[pos] == x:
                return pos
            elif arr[pos] < x:
                low = pos + 1
            else:
                high = pos - 1
        
        return -1  
    
    def binary_search(self, low, high, x):
        arr = self.heap_sort() 
        if high >= low:
            mid = low + (high - low) // 2  # Orta indeksi bul
            # Orta indeksteki değer aranan değerse, indeksi döndür
            if arr[mid] == x:
                return mid
            # Orta indeksteki değer aranan değerden büyükse, sol tarafa bak
            elif arr[mid] > x:
                return self.binary_search(low, mid - 1, x)
            # Orta indeksteki değer aranan değerden küçükse, sağ tarafa bak
            else:
                return self.binary_search(mid + 1, high, x)
        return -1  # Değer bulunamazsa -1 döndür
    
    def exponential_search(self,x):
        arr = self.heap_sort() 
        if arr[0] == x:  # İlk eleman aranan değerse, 0 döndür
            return 0
        i = 1
        # Aranan değerin bulunabileceği aralığı belirle
        while i < len(arr) and arr[i] <= x:
            i *= 2  # Üstel olarak aralığı genişlet
        # Bulunan aralıkta Binary Search uygula
        return self.binary_search(i // 2, min(i, len(arr) - 1), x)
    
def main():
    data = [random.randint(1, 1000000) for _ in range(1000000)]  # 1 milyon rastgele sayı 
    large_data_sorting_system = LargeDataSortingSystem(data)
    sorted_data = large_data_sorting_system.heap_sort()
    print("Heap Sort ile sıralanmış dizi:", sorted_data[:10])
    
    # sorted_data2=large_data_sorting_system.counting_sort()
    # print("Counting Sort ile sıralanmış dizi:",sorted_data2)
    
    x = random.randint(1, 1000000)
    search_x=large_data_sorting_system.interpolation_search(x)
    print(f"Interpolation Search ile {x}  bulunan indeks:", search_x)
    
    search_exponential=large_data_sorting_system.exponential_search(x)
    print("Exponential Search ile bulunan indeks:", search_exponential)
    
if __name__ == "__main__":
    main()
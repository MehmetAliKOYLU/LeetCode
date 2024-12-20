class Solution(object):
    def strStr(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        text_length = len(text)
        pattern_length = len(pattern)
        
        # Eğer alt metin boşsa, başlangıç indeksi 0 döner
        if pattern_length == 0:
            return 0
        
        # Eğer ana metin alt metinden kısa ise, eşleşme olamaz
        if text_length < pattern_length:
            return -1
        
        # Ana metin içinde alt metni kaydırarak ara
        for i in range(text_length - pattern_length + 1):
            # Eğer alt metin, mevcut konumda eşleşirse başlangıç indeksini döndür
            if text[i:i+pattern_length] == pattern:
                return i
        
        # Hiçbir eşleşme bulunamazsa -1 döner
        return -1

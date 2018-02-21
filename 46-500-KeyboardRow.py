class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ["QWERTYUIOPqwertyuiop", "ASDFGHJKLasdfghjkl", "ZXCVBNMzxcvbnm" ]
        res = []
        
        for x in words:
            a = None
            cont = True
            for y in x:
                if a == None:
                    for i,z in enumerate(keyboard):
                        if y in z:
                            a = i
                else:
                    if y not in keyboard[a]:
                        cont = False
                        break
            if cont:
                res.append(x)
        return res
                            
                        
                                    
                                    
                                    
                
                
        
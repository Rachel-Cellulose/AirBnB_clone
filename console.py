if args[0] in self.__classes:                                                                                                           
            if args[1] == "all()":                                                                                                              
                self.do_all(args[0])                                                                                                            
            elif args[1] == "count()":                                                                                                          
                _dict = storage.all().items()                                                                                                   
                list_ = [v for k, v in _dict if k.startswith(args[0])]                                                                          
                print(len(list_))                                                                                                               
            elif args[1].startswith("show"):                                                                                                    
                id_ = args[1].split('"')[1]                                                                                                     
                self.do_show(f"{args[0]} {id_}")                                                                                                
            elif args[1].startswith("destroy"):                                                                                                 
                id_ = args[1].split('"')[1]                                                                                                     
                self.do_destroy(f"{args[0]} {id_}")                                                                                             
            elif args[1].startswith("update"):                                                                                                  
                split_ = re.split('"update"|", "|\"', args[1])                                                                                  
                id_ = split_[1]                                                                                                                 
                attr_name = split_[2]                                                                                                           
                attr_value = split_[3]                                                                                                          
                self.do_update(f'{args[0]} {id_} {attr_name} "{attr_value}"')                                                                   
                                                                                                                                                
                                                                                                                                                
if __name__ == '__main__':                                                                                                                      
    HBNBCommand().cmdloop()

### press key for exiting video
1. 
without any press key
```
       if cv2.waitKey(1) & 0xFF == ord('x'):
        break
```


2.
press ESC key
```
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
```

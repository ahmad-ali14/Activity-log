# DOM

- `input.value` is alaways string, event if its type was number.
- client side temporary storage:

    ```js
    window.x = value;   => window.x;
    window.localStorage.x = value; => window.loacalStorage.x;
    ```

- add event listener to the key and use the key name intead of key code.

    ```javascript
    window.addEventListener("key-event", (event) => {
      event.key == "arrowLeft"; //you can use key name instead of key code.
    });
    ```

- make textarea with inly one line and disable multilines:
  `js <textarea rows="1" value ={ value } > { value } </textare> textarea.onChange = (e) => { let x = e.target.value; // deleting every new line signs from textarea value x.replace(/(\r\n|\n|\r)/gm, ""); }`

- sanitize third party code before inject it into your website using `innerHTML`

    ```javascript
    var sanitizeHTML = function (str) {
      var temp = document.createElement("div");
      temp.textContent = str;
      return temp.innerHTML;
    };
    ```

- quickly check existance of a file using vanilla js:

    ```javascript
    function doesFileExist(urlToFile) {
      var xhr = new XMLHttpRequest();
      xhr.open("HEAD", urlToFile, false);
      xhr.send();

      if (xhr.status == "404") {
        return false;
      } else {
        return true;
      }
    }
    ```
    
- control scrolling:

    ```js
    window.scrollTo(x, y); // x,y are the window cordinates.

    /* Using options: */

    window.scrollTo({ top: x, left: y, behavior: 'smooth' });
    ```
    
 - browser hsitory:

    ```js
    let x = window.history // Array of the nubmer of pages in the window history
    // you can go back and forth between pages
    x.goBack()
    x.foreward()

    // you can never extract the path from window.history
    ```
    
 - extract the url that you are coming from:
    
    ```js
    let x = document.referrer // "https://www.google.com/"
    
    // you were in google page and they refer you to here
    ```
    
 - window location:
    
    ```js
    // typical window.location object
    Location =  { 
        href: "https://www.w3schools.com/js/js_window_location.asp", 
        ancestorOrigins: DOMStringList, 
        origin: "https://www.w3schools.com", protocol: "https:",
        host: "www.w3schools.com", 
        pathname: "/js/js_window_location.asp"
    }
    ```

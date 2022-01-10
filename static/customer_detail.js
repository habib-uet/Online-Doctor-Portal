
      var x = document.getElementById("ad");
      
      function getLocation() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(showPosition);
        } else { 
          x.innerHTML = "Geolocation is not supported by this browser.";
        }
      }
      
      function showPosition(position) {
        document.getElementById("text-d4f2").value =   position.coords.latitude 
      }


var counter = 1;
setInterval(function(){
  document.getElementById('radio' + counter).checked = true;
  counter++;
  if(counter > 4){
    counter = 1;
    
  }
}, 4000);




    // const images = [
    //   "casa.jpg",
    //   "casa1.jpg",
    //   "logo.jpeg"
     
    //   // add more images as needed
    // ];
    
    // let currentIndex = 0;
    
    // const currentImage = document.getElementById("currentImage");
    // const nextImage = document.getElementById("nextImage");
    
    // setInterval(() => {
    //   currentImage.classList.add("opacity-0");
    //   currentImage.classList.remove("opacity-100");
    //   nextImage.classList.add("opacity-100");
    //   nextImage.classList.remove("opacity-0");
    
    //   const temp = currentImage.src;
    //   currentImage.src = nextImage.src;
    //   nextImage.src = temp;
    
    //   currentIndex = (currentIndex + 1) % images.length;
    //   nextImage.src = images[currentIndex];
    // }, 4000);


    
    // Definir una línea de números
// const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// // Recorrer la línea de inicio a fin
// console.log("Recorrido de inicio a fin:");
// for (let i = 0; i < numeros.length; i++) {
//   console.log(numeros[i]);
// }

// // Recorrer la línea de fin a inicio utilizando una estructura if
// console.log("Recorrido de fin a inicio:");
// for (let i = numeros.length - 1; i >= 0; i--) {
//   if (numeros[i] % 2 === 0) { // Si el número es par
//     console.log(numeros[i]);
//   }
// }

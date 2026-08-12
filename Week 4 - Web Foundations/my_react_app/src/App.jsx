import "./App.css";
import Course from "./Course";
import Footer from "./Footer";
import Navbar from "./Navbar";
import html from "./assets/HTML.jpg"
import css from "./assets/CSS.jpg"
import js from "./assets/js.jpg"


function App() {
  return (
    <>
     
      <Course name="HTML" price="$199" image={html}/>
      <Course name="CSS" price="$199" image={css}/>
      <Course name= "JS" price="$199" image={js} />
      
    </>
  );
}

export default App;
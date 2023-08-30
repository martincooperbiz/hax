import About from "./components/about";

import SEO from "./data/seo";
import { Helmet } from "react-helmet";

import "./App.css";

function App() {
  return (
    <div className="page-content">
      <div className="content-wrapper">
        <Helmet>
          <meta name="description" content={SEO.description} />
          <meta name="keywords" content={SEO.keywords.join(", ")} />
        </Helmet>

        <About />
      </div>
    </div>
  );
}

export default App;

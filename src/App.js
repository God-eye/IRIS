import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import {Button} from './components/Button/Button'
import { Header } from "./components/Header/Header";

function App() {
  return (
    <div className="App">
      <Router>
        <Header />
        <Switch>
          <Route exact path="/">
            <Button id="redbutton" buttonStyle="btn--red-outline" buttonSize='btn--large'>Home</Button> 
          </Route>
          <Route path='/ap'>
            <Button buttonStyle="btn--outline" buttonSize='btn--large'>SIGN UP</Button>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

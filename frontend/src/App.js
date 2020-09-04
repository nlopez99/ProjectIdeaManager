import React from 'react';
import { PageHeader, Avatar } from 'antd';
import { Login } from "./components/Login";
import { Home } from "./components/Home";
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import "./App.css"
import logo from "./logo.png";


export default function App() {

  const barIcon = <Avatar size="large" icon={logo} shape="square"/>

  return (
  <div>
    <PageHeader
      className="site-page-header"
      onBack={() => null}
      
    />
  <main>
    <Switch>
      <Route path="/" exact component={Login} />
      <Route path="/login" component={Login} />
      <Route path="/home" component={Home} />
    </Switch>
  </main>
  </div>
  );
  
}



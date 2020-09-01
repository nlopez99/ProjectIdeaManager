import React from 'react';
import { PageHeader } from 'antd';
import { Login } from "./components/Login";
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import "./App.css"


export default function App() {
  return (
  <div>
    <PageHeader
      className="site-page-header"
      onBack={() => null}
      title="Project Collector"
      style={{ color: 'white' }}
      
    />
  <main>
    <Switch>
      <Route path="/" exact />
      <Route path="/login" component={Login} />
    </Switch>
  </main>
  </div>
  );
  
}



import React from 'react';
import 'antd/dist/antd.css';
import './index.css';
import { Menu } from 'antd';
import { MailOutlined, AppstoreOutlined, SettingOutlined } from '@ant-design/icons';
import { Login } from "./components/Login"
const { SubMenu } = Menu;

class App extends React.Component {

  constructor() {
    super();
    this.state = {
      current: 'account',
      showTopMenu: true,
      showLogin: false,
    };
    this.hideComponent = this.hideComponent.bind(this);
  }

  hideComponent(name) {
    console.log(name);
    switch (name) {
      case "showTopMenu":
        this.setState({ showTopMenu: !this.state.showTopMenu });
        break;
      case "showLogin":
        this.setState({ showLogin: !this.state.showLogin });
        break;
      default:
        this.setState({ showLogin: !this.state.showLogin });
        this.setState({ showTopMenu: !this.state.showTopMenu });
        break;
    }
  }

  handleClick = e => {
    console.log('click ', e);
    this.setState({ current: e.key });
    }


  render() {
    const { current, showTopMenu, showLogin } = this.state;
    return (
      <Menu onClick={this.handleClick} selectedKeys={[current]} mode="horizontal">
        <Menu.Item key="account" icon={<SettingOutlined />}>
          Account
        </Menu.Item>
        <Menu.Item key="app" icon={<AppstoreOutlined />}>
          My Projects
        </Menu.Item>
        <SubMenu icon={<SettingOutlined />} title="Explore Projects">
          <Menu.ItemGroup title="Explore">
            <Menu.Item key="setting:1">Popular</Menu.Item>
            <Menu.Item key="setting:2">Trending</Menu.Item>
          </Menu.ItemGroup>
          <Menu.ItemGroup title="Search">
            <Menu.Item key="setting:3">Find by Name</Menu.Item>
            <Menu.Item key="setting:4">Advanced Search</Menu.Item>
          </Menu.ItemGroup>
        </SubMenu>
        <SubMenu icon={<SettingOutlined />} title="Share Projects">
          <Menu.ItemGroup title="Item 1">
            <Menu.Item key="setting:1">Option 1</Menu.Item>
            <Menu.Item key="setting:2">Option 2</Menu.Item>
          </Menu.ItemGroup>
          <Menu.ItemGroup title="Item 2">
            <Menu.Item key="setting:3">Option 3</Menu.Item>
            <Menu.Item key="setting:4">Option 4</Menu.Item>
          </Menu.ItemGroup>
        </SubMenu>
      </Menu>
    );
    
  }
};

export default App;
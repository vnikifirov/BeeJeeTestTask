import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewTaskForm extends React.Component {
  state = {
    id: 0,
    userName: "",
    email: "",
    textTask: "",
    statusTask: ""
  };

  componentDidMount() {
    if (this.props.task) {
      const { id, userName, textTask, email, statusTask  } = this.props.task;
      this.setState({ id, userName, textTask, email, statusTask });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createTask = e => {
    e.preventDefault();
    axios.post(API_URL + "/task-create/", this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editTask = e => {
    e.preventDefault();
    axios.post(API_URL + "/task-update/" + this.state.id + "/", this.state,  {
      headers: {
        Authorization: `JWT ${localStorage.getItem('token')}`
      }
    }).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.task ? this.editTask : this.createTask}>
        <FormGroup>
          <Label for="userName">Name:</Label>
          <Input
            type="text"
            name="userName"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.userName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="textTask">Text:</Label>
          <Input
            type="text"
            name="textTask"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.textTask)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="phone">Status:</Label>
          <Input
            type="text"
            name="statusTask"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.statusTask)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewTaskForm;
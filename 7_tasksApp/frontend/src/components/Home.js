import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import TaskList from "./TaskList";
import NewTaskModal from "./NewTaskModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    task: [],
    nextPageURL: ''
  };

  nextPage  =  this.nextPage.bind(this);

  nextPage() {
    var  self  =  this;
    const url = `${API_URL}${self.state.nextPageURL}`
    axios.get(url).then(response => response.data).then((result) => {
        self.setState({ task:  result.data, nextPageURL:  result.nextlink})
    });
  }

  componentDidMount() {
    this.resetState();
  }

  getTask = () => {
    axios.get(API_URL + "/task-list").then(result => this.setState({ task:  result.data.data, nextPageURL: result.data.nextlink }));
  };

  resetState = () => {
    this.getTask();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <TaskList
              task={this.state.task}
              resetState={this.resetState}
            />
          </Col>
          <button className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </Row>
        <Row>
          <Col>
            <NewTaskModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;
import React, { Component } from "react";
import { Table } from "reactstrap";
import NewTaskModal from "./NewTaskModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class TaskList extends Component {
  render() {
    const task = this.props.task;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Text</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!task || task.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            task.map(task => (
              <tr key={task.id}>
                <td>{task.userName}</td>
                <td>{task.email}</td>
                <td>{task.textTask}</td>
                <td>{task.statusTask}</td>
                <td align="center">
                  <NewTaskModal
                    create={false}
                    task={task}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    id={task.id}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default TaskList;
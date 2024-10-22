import React from 'react';
import { Button } from 'react-bootstrap';

const TestCaseRow = ({ testCase, handleDelete }) => (
  <tr>
    <td>{testCase.id}</td>
    <td>{testCase.name}</td>
    <td>{testCase.description}</td>
    <td>{testCase.steps.join(', ')}</td>
    <td>{testCase.expected_result}</td>
    <td>{testCase.priority}</td>
    <td>
      <Button variant="danger" onClick={() => handleDelete(testCase.id)}>Удалить</Button>
    </td>
  </tr>
);

export default TestCaseRow;
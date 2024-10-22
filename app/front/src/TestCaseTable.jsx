import React from 'react';
import { Table } from 'react-bootstrap';
import TestCaseRow from './TestCaseRow';

const TestCaseTable = ({ testCases, handleDelete }) => (
  <Table striped bordered hover>
    <thead>
      <tr>
        <th>Ай-ди</th>
        <th>Имя</th>
        <th>Описание</th>
        <th>Шаги</th>
        <th>Ожидаемый результат</th>
        <th>Приоритет</th>
        <th>Действие</th>
      </tr>
    </thead>
    <tbody>
      {testCases.map(tc => (
        <TestCaseRow key={tc.id} testCase={tc} handleDelete={handleDelete} />
      ))}
    </tbody>
  </Table>
);

export default TestCaseTable;
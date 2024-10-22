import React from 'react';
import { Form, Button } from 'react-bootstrap';

const TestCaseForm = ({ testCase, handleChange, handleSubmit }) => (
  <Form onSubmit={handleSubmit} className="mb-4">
    <Form.Group controlId="name" className="mb-2">
      <Form.Label>Имя</Form.Label>
      <Form.Control type="text" name="name" value={testCase.name} onChange={handleChange} />
    </Form.Group>

    <Form.Group controlId="description" className="mb-2">
      <Form.Label>Описание</Form.Label>
      <Form.Control type="text" name="description" value={testCase.description} onChange={handleChange} />
    </Form.Group>

    <Form.Group controlId="steps" className="mb-2">
      <Form.Label>Шаги (через запятую)</Form.Label>
      <Form.Control type="text" name="steps" value={testCase.steps} onChange={handleChange} />
    </Form.Group>

    <Form.Group controlId="expected_result" className="mb-2">
      <Form.Label>Ожидаемый результат</Form.Label>
      <Form.Control type="text" name="expected_result" value={testCase.expected_result} onChange={handleChange} />
    </Form.Group>

    <Form.Group controlId="priority" className="mb-2">
      <Form.Label>Приоритет</Form.Label>
      <Form.Select name="priority" value={testCase.priority} onChange={handleChange}>
        <option>низкий</option>
        <option>средний</option>
        <option>высокий</option>
      </Form.Select>
    </Form.Group>

    <Button type="submit">Add Test Case</Button>
  </Form>
);

export default TestCaseForm;
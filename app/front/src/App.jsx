import React, { useState, useEffect } from 'react';
import { Container, Alert } from 'react-bootstrap';
import TestCaseForm from './TestCaseFrom';
import TestCaseTable from './TestCaseTable';
import { fetchTestCases, createTestCase, deleteTestCase } from './api';

const App = () => {
  const [testCases, setTestCases] = useState([]);
  const [testCase, setTestCase] = useState({
    name: '',
    description: '',
    steps: '',
    expected_result: '',
    priority: 'средний',
  });
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadTestCases = async () => {
      try {
        const data = await fetchTestCases();
        setTestCases(data);
      } catch (err) {
        setError(err.message);
      }
    };
    loadTestCases();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setTestCase({ ...testCase, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newTestCase = await createTestCase(testCase);
      setTestCases([...testCases, newTestCase]);
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteTestCase(id);
      setTestCases(testCases.filter(tc => tc.id !== id));
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <Container>
      <h1 className="mt-4">Импортзамещенная тестовая система</h1>
      {error && <Alert variant="danger">{error}</Alert>}
      <TestCaseForm testCase={testCase} handleChange={handleChange} handleSubmit={handleSubmit} />
      <TestCaseTable testCases={testCases} handleDelete={handleDelete} />
    </Container>
  );
};

export default App;
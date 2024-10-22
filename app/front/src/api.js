const apiUrl = 'http://app_api:8000/testcases';

export const fetchTestCases = async () => {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error(`Error fetching test cases: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const createTestCase = async (testCase) => {
  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...testCase, steps: testCase.steps.split(',') }),
    });
    if (!response.ok) {
      throw new Error(`Error creating test case: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
};

export const deleteTestCase = async (id) => {
  try {
    const response = await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    if (!response.ok) {
      throw new Error(`Error deleting test case: ${response.statusText}`);
    }
  } catch (error) {
    console.error(error);
    throw error;
  }
};
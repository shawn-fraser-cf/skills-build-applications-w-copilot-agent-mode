import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Fetching Workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched Workouts:', results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, []);
  return (
    <div>
      <h2 className="mb-4 text-danger">Workouts</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-light">
            <tr>
              {workouts.length > 0 && Object.keys(workouts[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {workouts.map((workout, idx) => (
              <tr key={workout.id || idx}>
                {workouts.length > 0 && Object.keys(workouts[0]).map((key) => (
                  <td key={key}>{String(workout[key])}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        {workouts.length === 0 && <div className="alert alert-info">No workouts found.</div>}
      </div>
    </div>
  );
};

export default Workouts;

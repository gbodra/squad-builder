import { useCallback } from "react";
import { Handle, Position } from "reactflow";

function AgentNode({ data, isConnectable }) {
  const onChange = useCallback((evt) => {
    console.log(evt.target.value);
  }, []);

  return (
    <div className="text-updater-node">
      <Handle
        type="target"
        position={Position.Top}
        isConnectable={isConnectable}
      />
      <div className="card">
        <div className="card-header text-center bg-primary text-white">
          <i className="bi bi-robot"></i> Agent
        </div>
        <div className="card-body">
          <h5 className="card-title">
            <div className="input-group mb-3">
              <span className="input-group-text" id="basic-addon1">
                Role
              </span>
              <input
                type="text"
                className="form-control"
                placeholder="CTO"
                aria-label="role"
                aria-describedby="basic-addon1"
              />
            </div>
          </h5>
          <p className="card-text">
            <div className="input-group mb-3">
              <span className="input-group-text" id="basic-addon1">
                Goal
              </span>
              <input
                type="text"
                className="form-control"
                placeholder="Provide technical leadership."
                aria-label="goal"
                aria-describedby="basic-addon1"
              />
            </div>
            <div className="input-group mb-3">
              <span className="input-group-text" id="basic-addon1">
                Backstory
              </span>
              <textarea
                className="form-control"
                aria-label="backstory"
                placeholder="Worked at Google for 10 years."
              ></textarea>
            </div>
          </p>
        </div>
      </div>
      <Handle
        type="source"
        position={Position.Bottom}
        isConnectable={isConnectable}
      />
    </div>
  );
}

export default AgentNode;

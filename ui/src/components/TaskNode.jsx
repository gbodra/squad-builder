import { useCallback } from "react";
import { Handle, Position } from "reactflow";

function TaskNode({ data, isConnectable }) {
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
        <div className="card-header text-center bg-danger text-white">
          <i className="bi bi-list-task"></i> Task
        </div>
        <div className="card-body">
          <h5 className="card-title">
            <div className="input-group mb-3">
              <span className="input-group-text" id="basic-addon1">
                Description
              </span>
              <textarea
                className="form-control"
                aria-label="description"
                placeholder="Describe the task you want your agent to perform."
              ></textarea>
            </div>
          </h5>
          <p className="card-text">
            <div className="input-group mb-3">
              <span className="input-group-text" id="basic-addon1">
                Expected output
              </span>
              <textarea
                className="form-control"
                aria-label="output"
                placeholder="Describe how you expect your agent to format the answer."
              ></textarea>
            </div>
            <div className="row">
              <div className="col-6">
                <div className="form-check form-switch">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    role="switch"
                    id="flexSwitchCheckDefault"
                    checked
                  />
                  <label
                    className="form-check-label"
                    htmlFor="flexSwitchCheckDefault"
                  >
                    Web search
                  </label>
                </div>
                <div className="form-check form-switch">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    role="switch"
                    id="flexSwitchCheckDefault"
                  />
                  <label
                    className="form-check-label"
                    htmlFor="flexSwitchCheckDefault"
                  >
                    Read PDF
                  </label>
                </div>
              </div>
              <div className="col-6">
                <div className="form-check form-switch">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    role="switch"
                    id="flexSwitchCheckDefault"
                  />
                  <label
                    className="form-check-label"
                    htmlFor="flexSwitchCheckDefault"
                  >
                    Read CSV
                  </label>
                </div>
                <div className="form-check form-switch">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    role="switch"
                    id="flexSwitchCheckDefault"
                    checked
                  />
                  <label
                    className="form-check-label"
                    htmlFor="flexSwitchCheckDefault"
                  >
                    Generate PDF
                  </label>
                </div>
              </div>
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

export default TaskNode;

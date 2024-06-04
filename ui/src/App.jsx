import { useCallback } from "react";
import ReactFlow, {
  MiniMap,
  Panel,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
} from "reactflow";

import "reactflow/dist/style.css";
import { nanoid } from "nanoid";
import AgentNode from "./components/AgentNode.jsx";
import TaskNode from "./components/TaskNode.jsx";

const screenWidth = window.innerWidth - 400;
const screenHeight = window.innerHeight - 400;

const initialNodes = [
  {
    id: "1",
    type: "agentNode",
    position: { x: screenWidth / 2, y: screenHeight / 2 },
  },
  {
    id: "2",
    type: "taskNode",
    position: { x: screenWidth / 2, y: screenHeight / 2 + 300 },
  },
];
const initialEdges = [{ id: "e1-2", source: "1", target: "2" }];

const nodeTypes = { agentNode: AgentNode, taskNode: TaskNode };

export default function App() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  const addNode = (type) => {
    const newNode = {
      id: nanoid(),
      type,
      position: { x: Math.random() * 400, y: Math.random() * 400 },
      data: { label: `${type} node` },
    };

    setNodes((es) => es.concat(newNode));
  };

  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
      >
        <Panel position="top-left">
          <div className="card">
            <div className="card-header">Toolbox</div>
            <div className="card-body">
              <p className="card-text">
                <div
                  className="btn-group-vertical"
                  role="group"
                  aria-label="Vertical button group"
                >
                  <button
                    className="btn btn-primary"
                    onClick={() => addNode("agentNode")}
                  >
                    <i className="bi bi-robot"></i> Add Agent
                  </button>
                  <button
                    className="btn btn-danger"
                    onClick={() => addNode("taskNode")}
                  >
                    <i className="bi bi-list-task"></i> Add Task
                  </button>
                </div>
              </p>
            </div>
          </div>
        </Panel>
        <Controls />
        <MiniMap />
        <Background variant="dots" gap={12} size={1} />
      </ReactFlow>
    </div>
  );
}

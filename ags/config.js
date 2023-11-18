// Imports
const { Hyprland } = ags.Service;
// const { App } = ags;
const { exec, execAsync } = ags.Utils;
const {
  Box,
  Button,
  Overlay,
  // Stack,
  Label,
  // Icon,
  CenterBox,
  Window,
  // Slider,
  // ProgressBar,
} = ags.Widget;

// Constants
const scss = ags.App.configDir + "/style.scss";
const css = ags.App.configDir + "/style.css";

exec(`sassc ${scss} ${css}`);

// Widgets
const Workspaces = () =>
  Box({
    className: "workspaces",
    connections: [
      [
        Hyprland,
        (box) => {
          const arr = Array.from({ length: 9 }, (_, i) => i + 1);
          box.children = arr.map((i) =>
            Button({
              onClicked: () => execAsync(`hyprctl dispatch workspace ${i}`),
              className: "workspace",
              child: Label(
                (() => {
                  let label;
                  let workspaceWindows = (
                    Hyprland.workspaces.get(i) ?? { windows: 0 }
                  ).windows;
                  if (Hyprland.active.workspace.id == i) {
                    label = {
                      label: "󰮯",
                      className: "icon selected",
                    };
                  } else if (workspaceWindows > 0) {
                    label = {
                      label: "󰊠",
                      className: "icon occupied",
                    };
                  } else {
                    label = {
                      label: "󰧟",
                      className: "icon empty",
                    };
                  }
                  return label;
                })(),
              ),
            }),
          );
        },
      ],
    ],
  });

const WorkspacesDemo = () =>
  Box({
    className: "workspaces",
    connections: [
      [
        Hyprland,
        (box) => {
          // generate an array [1..10] then make buttons from the index
          const arr = Array.from({ length: 10 }, (_, i) => i + 1);
          box.children = arr.map((i) =>
            Button({
              onClicked: () => execAsync(`hyprctl dispatch workspace ${i}`),
              child: Label({ label: `${i}` }),
              // child: Label({ label: Hyprland.active.workspace.id == i ? "󰮯" : "󰧟" }),
              className: Hyprland.active.workspace.id == i ? "focused" : "",
            }),
          );
        },
      ],
    ],
  });

const RightSeparator = (left, right) =>
  Overlay({
    child: Label({ label: "          " }),
    overlays: [
      Label({
        label: "",
        style: `color: ${left}`,
        className: "separator",
        halign: "start",
      }),
      Label({
        label: "",
        style: `color: ${right}`,
        className: "separator",
        halign: "end",
      }),
    ],
  });

const LeftSeparator = (left, right) =>
  Overlay({
    child: Label({ label: "          " }),
    overlays: [
      Label({
        label: "",
        style: `color: ${left}`,
        className: "separator",
        halign: "start",
      }),
      Label({
        label: "",
        style: `color: ${right}`,
        className: "separator",
        halign: "end",
      }),
    ],
  });

const TestButton = () =>
  Button({
    onPrimaryClick: () =>
      execAsync("notify-send -u normal -t 30000 -a AGS-WIP Debug meme"),
    // onPrimaryClick: () => console.log('Clicked!'),
    child: Label("Click me!"),
  });

const TestHypr = () =>
  Button({
    connections: [
      [
        Hyprland,
        (button) =>
        (button.onClicked = () =>
          execAsync(
            `notify-send -u normal -t 5000 -a AGS-WIP Hyprland-debug ${JSON.stringify(
              (Hyprland.workspaces.get(1) ?? { windows: 0 }).windows,
            )}`,
          )),
      ],
    ],
    child: Label("Hyprland"),
  });

const TestLabel = () => Label("Greetings!");

// Layouts
const Left = () =>
  Box({
    halign: "start",
    className: "section",
    children: [TestButton(), TestLabel()],
  });

const Center = () =>
  Box({
    className: "section",
    children: [Workspaces()],
  });

const Right = () =>
  Box({
    halign: "end",
    className: "section",
    children: [
      Label({
        label: "",
        style: "color: #363d5c",
        className: "separator",
        halign: "end",
      }),
      Label({ label: "extra", className: "testLabel" }),
      RightSeparator("#363d5c", "#363d5c"),
      Label({ label: "bright/vol", className: "testLabel" }),
      RightSeparator("#363d5c", "#363d5c"),
      Label({ label: "system", className: "testLabel" }),
      RightSeparator("#363d5c", "#363d5c"),
      Label({ label: "batteries", className: "testLabel" }),
      RightSeparator("#363d5c", "#ff8400"),
      Label({
        // label: "time",
        className: "testLabel end",
        connections: [
          [1000, label => label.label = exec('date')]
        ],
      }),
    ],
  });

// Windows
const Bar = ({ monitor } = {}) =>
  Window({
    name: `bar${monitor ?? ""}`,
    className: "window",
    monitor,
    anchor: ["top", "left", "right"],
    exclusive: true,
    child: CenterBox({
      className: "bar",
      startWidget: Left(),
      centerWidget: Center(),
      endWidget: Right(),
    }),
  });

// Export the environment
export default {
  style: css,
  windows: [
    Bar({ monitor: 0 }),
    // Bar({ monitor: 1 }),
    // Bar({ monitor: 2 })
  ],
};

import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export type ComparisonCardProps = {
  title: string;
  labels: [string, string, string];
  values: [number, number, number];
  conclusion: string;
};

const palette = ["#CF5B3E", "#D8A43A", "#2A7E7B"] as const;

export const ComparisonCard: React.FC<ComparisonCardProps> = ({
  title,
  labels,
  values,
  conclusion,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const entry = spring({
    fps,
    frame,
    config: { damping: 18, stiffness: 130, mass: 0.8 },
  });
  const maxValue = Math.max(...values, 1);

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#F4F0E7",
        color: "#20201E",
        fontFamily: "sans-serif",
      }}
    >
      <div
        style={{
          width: 820,
          padding: 56,
          border: "3px solid #20201E",
          borderRadius: 28,
          backgroundColor: "#FFFDF7",
          boxShadow: "16px 16px 0 #20201E",
          transform: "scale(" + interpolate(entry, [0, 1], [0.92, 1]) + ")",
          opacity: entry,
        }}
      >
        <div style={{ fontSize: 42, fontWeight: 800, marginBottom: 38 }}>
          {title}
        </div>
        <div style={{ display: "flex", gap: 24, alignItems: "end" }}>
          {values.map((value, index) => {
            const barProgress = interpolate(
              frame,
              [12 + index * 7, 30 + index * 7],
              [0, value / maxValue],
              {
                easing: Easing.out(Easing.cubic),
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              },
            );
            const height = Math.max(24, 280 * barProgress);

            return (
              <div
                key={labels[index]}
                style={{ flex: 1, display: "flex", flexDirection: "column", gap: 12 }}
              >
                <div style={{ minHeight: 70, fontSize: 28, fontWeight: 700 }}>
                  {labels[index]}
                </div>
                <div
                  style={{
                    height,
                    borderRadius: "18px 18px 0 0",
                    backgroundColor: palette[index],
                    display: "flex",
                    alignItems: "flex-start",
                    justifyContent: "center",
                    paddingTop: 18,
                    color: "#FFFDF7",
                    fontSize: 38,
                    fontWeight: 900,
                  }}
                >
                  {value}
                </div>
              </div>
            );
          })}
        </div>
        <div
          style={{
            marginTop: 34,
            borderTop: "2px solid #20201E",
            paddingTop: 22,
            fontSize: 30,
            lineHeight: 1.35,
            fontWeight: 700,
          }}
        >
          {conclusion}
        </div>
      </div>
    </AbsoluteFill>
  );
};

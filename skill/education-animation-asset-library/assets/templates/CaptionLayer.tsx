import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export type CaptionLayerProps = {
  text: string;
  emphasis?: string;
  fromFrame: number;
  durationInFrames: number;
};

export const CaptionLayer: React.FC<CaptionLayerProps> = ({
  text,
  emphasis,
  fromFrame,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const localFrame = frame - fromFrame;
  const opacity = interpolate(
    localFrame,
    [0, Math.round(fps * 0.16), durationInFrames - Math.round(fps * 0.12), durationInFrames],
    [0, 1, 1, 0],
    {
      easing: Easing.out(Easing.cubic),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  const renderText = () => {
    if (!emphasis || !text.includes(emphasis)) return text;
    const [before, after] = text.split(emphasis);
    return (
      <>
        {before}
        <span style={{ color: "#F0C04B" }}>{emphasis}</span>
        {after}
      </>
    );
  };

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "flex-end",
        padding: "0 72px 240px",
        pointerEvents: "none",
      }}
    >
      <div
        style={{
          maxWidth: 900,
          color: "#FFFFFF",
          fontFamily: "sans-serif",
          fontSize: 50,
          lineHeight: 1.26,
          fontWeight: 800,
          letterSpacing: 1,
          textAlign: "center",
          textShadow: "0 3px 0 #151515, 0 0 16px rgba(0,0,0,0.7)",
          opacity,
        }}
      >
        {renderText()}
      </div>
    </AbsoluteFill>
  );
};

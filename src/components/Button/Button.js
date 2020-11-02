import React from "react";
import "./Button.css";
import { Link } from "react-router-dom";

const STYLES = ["btn--primary", "btn--outline", "btn--red-primary", "btn--green-primary","btn--red-outline", "btn--green-outline"];

const SIZES = ["btn--medium", "btn--large"];

export const Button = ({
  children,
  type,
  id,
  onClick,
  buttonStyle,
  buttonSize,

}) => {
  const checkButtonStyle = STYLES.includes(buttonStyle)
    ? buttonStyle
    : STYLES[0];

  const checkButtonSize = SIZES.includes(buttonSize) ? buttonSize : SIZES[0];

  return (
    <Link to="/sign-up" className="btn-mobile">
      <button
        className={`btn ${checkButtonStyle} ${checkButtonSize}`}
        id={id}
        onClick={onClick}
        type={type}
      >
        {children}
      </button>
    </Link>
  );
};

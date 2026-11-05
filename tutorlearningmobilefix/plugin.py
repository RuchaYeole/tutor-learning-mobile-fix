from tutor import hooks

MOBILE_FIX_CSS = """
/* Mobile and tablet responsiveness */
@media screen and (max-width: 767px) {

    /* Prevent horizontal overflow */
    html,
    body {
        max-width: 100%;
        overflow-x: hidden;
    }

    /* Make course sidebar fit the screen */
    .outline-sidebar-wrapper.fixed-top,
    #course-sidebar.fixed-top,
    section[data-testid^="sidebar-"].fixed-top {
        position: relative !important;
        top: auto !important;
        right: auto !important;
        bottom: auto !important;
        left: auto !important;
        width: 100% !important;
        height: auto !important;
        max-height: none !important;
        overflow: visible !important;
    }

    /* Stack course content vertically */
    .sequence-container.d-inline-flex.flex-row {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
    }

    /* Keep content within viewport */
    .unit-container,
    .sequence-container,
    .course-content {
        max-width: 100% !important;
        box-sizing: border-box;
    }

    /* Make embedded media responsive */
    img,
    video,
    iframe {
        max-width: 100%;
    }
}

/* Tablet layout */
@media screen and (min-width: 768px) and (max-width: 1199px) {
    .sequence-container.d-inline-flex.flex-row {
        flex-wrap: wrap !important;
    }
}
"""

hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-dockerfile-pre-npm-build-learning",
        "RUN cat >> /openedx/app/src/index.scss <<'LEARNINGMOBILEFIX_EOF'\n"
        f"{MOBILE_FIX_CSS}\n"
        "LEARNINGMOBILEFIX_EOF",
    )
)

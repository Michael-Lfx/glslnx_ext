#version 410 core

uniform float fGlobalTime; // in seconds
uniform vec2 v2Resolution; // viewport resolution (in pixels)

layout(location = 0) out vec4 out_color; // out_color must be written in order to see anything

void main(void)
{
    vec2 uv = (gl_FragCoord.xy / v2Resolution.xy) - vec2(0.5);
    uv.x *= v2Resolution.x / v2Resolution.y;

    vec3 ro = vec3(0.0, 0.0, 1.5);
    vec3 rd = normalize(vec3(uv, -1.5));
    bool hit = false;
    vec4 res = spheretrace(ro, rd, hit);
    if(hit)
        out_color = vec4(1.0);
    else
        out_color = vec4(0.05) * (1.0 - length(uv));
}
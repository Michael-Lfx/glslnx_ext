#version 410 core

float SDF(in vec3 p)
{
    return length(p) - 0.35;
}
//-------------------------//
#define MAX_DISTANCE 512.0
#define MAX_STEPS 256
#define EPSILON 0.001

vec4 spheretrace(in vec3 ro, in vec3 rd, out bool hit)
{
    vec3 p = ro;
    float d = SDF(p);
    float dAcc = d;
    hit = false;
    for(int i = 0; i < MAX_STEPS; ++i)
    {
        if(d <= EPSILON || d >= MAX_DISTANCE)
        {
            hit = d <= EPSILON;
            break;
        }

        p += d * rd;
        d = SDF(p);
        dAcc += d;
    }
    return vec4(p, dAcc);
}
//-------------------------//

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
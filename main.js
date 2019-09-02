function decode64(t) {
    var e, i, n, o, r, a = "", s = "", l = "", h = 0;
    do {
        n = keyStr.indexOf(t.charAt(h++)),
            o = keyStr.indexOf(t.charAt(h++)),
            r = keyStr.indexOf(t.charAt(h++)),
            l = keyStr.indexOf(t.charAt(h++)),
            e = n << 2 | o >> 4,
            i = (15 & o) << 4 | r >> 2,
            s = (3 & r) << 6 | l,
            a += String.fromCharCode(e),
        64 != r && (a += String.fromCharCode(i)),
        64 != l && (a += String.fromCharCode(s)),
            e = i = s = "",
            n = o = r = l = ""
    } while (h < t.length);
    return a
}

// var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
"undefined" == typeof a3d && (a3d = {}),
    function () {
        var t = !1
            , e = /xyz/.test(function () {
            xyz
        }) ? /\b_super\b/ : /.*/;
        this.Class = function () {
        }
            ,
            Class.extend = function (i) {
                function n() {
                    !t && this.init && this.init.apply(this, arguments)
                }

                var o = this.prototype;
                t = !0;
                var r = new this;
                t = !1;
                for (var a in i)
                    r[a] = "function" == typeof i[a] && "function" == typeof o[a] && e.test(i[a]) ? function (t, e) {
                        return function () {
                            var i = this._super;
                            this._super = o[t];
                            var n = e.apply(this, arguments);
                            return this._super = i,
                                n
                        }
                    }(a, i[a]) : i[a];
                return n.prototype = r,
                    n.constructor = n,
                    n.extend = arguments.callee,
                    n
            }
    }(),
    a3d.Endian = {
        BIG: 0,
        LITTLE: 1
    },
    a3d.ByteArray = Class.extend({
        data: "",
        length: 0,
        pos: 0,
        pow: Math.pow,
        endian: a3d.Endian.BIG,
        TWOeN23: Math.pow(2, -23),
        TWOeN52: Math.pow(2, -52),
        init: function (t, e) {
            this.data = void 0 !== t ? t : "",
            void 0 !== e && (this.endian = e),
                this.length = t.length;
            var i = e == a3d.Endian.BIG ? "BE" : "LE"
                , n = ["readInt32", "readInt16", "readUInt32", "readUInt16", "readFloat32", "readFloat64"];
            for (var o in n)
                this[n[o]] = this[n[o] + i];
            var r = {
                readUnsignedByte: "readByte",
                readUnsignedInt: "readUInt32",
                readFloat: "readFloat32",
                readDouble: "readFloat64",
                readShort: "readInt16",
                readBoolean: "readBool",
                readInt: "readInt32"
            };
            for (var o in r)
                this[o] = this[r[o]]
        },
        readByte: function () {
            return 255 & this.data.charCodeAt(this.pos++)
        },
        readBool: function () {
            return !!(255 & this.data.charCodeAt(this.pos++))
        },
        readUInt32BE: function () {
            var t = this.data
                , e = (this.pos += 4) - 4;
            return (255 & t.charCodeAt(e)) << 24 | (255 & t.charCodeAt(++e)) << 16 | (255 & t.charCodeAt(++e)) << 8 | 255 & t.charCodeAt(++e)
        },
        readInt32BE: function () {
            var t = this.data
                , e = (this.pos += 4) - 4
                ,
                i = (255 & t.charCodeAt(e)) << 24 | (255 & t.charCodeAt(++e)) << 16 | (255 & t.charCodeAt(++e)) << 8 | 255 & t.charCodeAt(++e);
            return i >= 2147483648 ? i - 4294967296 : i
        },
        readUInt16BE: function () {
            var t = this.data
                , e = (this.pos += 2) - 2;
            return (255 & t.charCodeAt(e)) << 8 | 255 & t.charCodeAt(++e)
        },
        readInt16BE: function () {
            var t = this.data
                , e = (this.pos += 2) - 2
                , i = (255 & t.charCodeAt(e)) << 8 | 255 & t.charCodeAt(++e);
            return i >= 32768 ? i - 65536 : i
        },
        readFloat32BE: function () {
            var t = this.data
                , e = (this.pos += 4) - 4
                , i = 255 & t.charCodeAt(e)
                , n = 255 & t.charCodeAt(++e)
                , o = 255 & t.charCodeAt(++e)
                , r = 255 & t.charCodeAt(++e)
                , a = 1 - (i >> 7 << 1)
                , s = (i << 1 & 255 | n >> 7) - 127
                , l = (127 & n) << 16 | o << 8 | r;
            return 0 == l && -127 == s ? 0 : a * (1 + this.TWOeN23 * l) * this.pow(2, s)
        },
        readFloat64BE: function () {
            var t = this.data
                , e = (this.pos += 8) - 8
                , i = 255 & t.charCodeAt(e)
                , n = 255 & t.charCodeAt(++e)
                , o = 255 & t.charCodeAt(++e)
                , r = 255 & t.charCodeAt(++e)
                , a = 255 & t.charCodeAt(++e)
                , s = 255 & t.charCodeAt(++e)
                , l = 255 & t.charCodeAt(++e)
                , h = 255 & t.charCodeAt(++e)
                , u = 1 - (i >> 7 << 1)
                , c = (i << 4 & 2047 | n >> 4) - 1023
                ,
                p = ((15 & n) << 16 | o << 8 | r).toString(2) + (a >> 7 ? "1" : "0") + ((127 & a) << 24 | s << 16 | l << 8 | h).toString(2);
            return p = parseInt(p, 2),
                0 == p && -1023 == c ? 0 : u * (1 + this.TWOeN52 * p) * this.pow(2, c)
        },
        readUInt32LE: function () {
            var t = this.data
                , e = this.pos += 4;
            return (255 & t.charCodeAt(--e)) << 24 | (255 & t.charCodeAt(--e)) << 16 | (255 & t.charCodeAt(--e)) << 8 | 255 & t.charCodeAt(--e)
        },
        readInt32LE: function () {
            var t = this.data
                , e = this.pos += 4
                ,
                i = (255 & t.charCodeAt(--e)) << 24 | (255 & t.charCodeAt(--e)) << 16 | (255 & t.charCodeAt(--e)) << 8 | 255 & t.charCodeAt(--e);
            return i >= 2147483648 ? i - 4294967296 : i
        },
        readUInt16LE: function () {
            var t = this.data
                , e = this.pos += 2;
            return (255 & t.charCodeAt(--e)) << 8 | 255 & t.charCodeAt(--e)
        },
        readInt16LE: function () {
            var t = this.data
                , e = this.pos += 2
                , i = (255 & t.charCodeAt(--e)) << 8 | 255 & t.charCodeAt(--e);
            return i >= 32768 ? i - 65536 : i
        },
        readFloat32LE: function () {
            var t = this.data
                , e = this.pos += 4
                , i = 255 & t.charCodeAt(--e)
                , n = 255 & t.charCodeAt(--e)
                , o = 255 & t.charCodeAt(--e)
                , r = 255 & t.charCodeAt(--e)
                , a = 1 - (i >> 7 << 1)
                , s = (i << 1 & 255 | n >> 7) - 127
                , l = (127 & n) << 16 | o << 8 | r;
            return 0 == l && -127 == s ? 0 : a * (1 + this.TWOeN23 * l) * this.pow(2, s)
        },
        readFloat64LE: function () {
            var t = this.data
                , e = this.pos += 8
                , i = 255 & t.charCodeAt(--e)
                , n = 255 & t.charCodeAt(--e)
                , o = 255 & t.charCodeAt(--e)
                , r = 255 & t.charCodeAt(--e)
                , a = 255 & t.charCodeAt(--e)
                , s = 255 & t.charCodeAt(--e)
                , l = 255 & t.charCodeAt(--e)
                , h = 255 & t.charCodeAt(--e)
                , u = 1 - (i >> 7 << 1)
                , c = (i << 4 & 2047 | n >> 4) - 1023
                ,
                p = ((15 & n) << 16 | o << 8 | r).toString(2) + (a >> 7 ? "1" : "0") + ((127 & a) << 24 | s << 16 | l << 8 | h).toString(2);
            return p = parseInt(p, 2),
                0 == p && -1023 == c ? 0 : u * (1 + this.TWOeN52 * p) * this.pow(2, c)
        },
        readUInt64LE: function () {
            var t = this.data
                , e = this.pos
                ,
                i = (255 & t.charCodeAt(e + 3)) << 24 | (255 & t.charCodeAt(e + 2)) << 16 | (255 & t.charCodeAt(e + 1)) << 8 | 255 & t.charCodeAt(e)
                ,
                n = (255 & t.charCodeAt(e + 7)) << 24 | (255 & t.charCodeAt(e + 6)) << 16 | (255 & t.charCodeAt(e + 5)) << 8 | 255 & t.charCodeAt(e + 4);
            return this.pos += 8,
            65536 * n * 65536 + i
        },
        readInt64LE: function () {
            var t = this.data
                , e = this.pos
                ,
                i = (255 & t.charCodeAt(e + 3)) << 24 | (255 & t.charCodeAt(e + 2)) << 16 | (255 & t.charCodeAt(e + 1)) << 8 | 255 & t.charCodeAt(e)
                ,
                n = (255 & t.charCodeAt(e + 7)) << 24 | (255 & t.charCodeAt(e + 6)) << 16 | (255 & t.charCodeAt(e + 5)) << 8 | 255 & t.charCodeAt(e + 4);
            this.pos += 8;
            var o = 65536 * n * 65536 + i;
            return o > 0x8000000000000000 && (o -= 0x10000000000000000),
                o
        },
        readUTF: function () {
            for (var t = this.readUInt16LE(), e = []; t > 0;) {
                var i = this.readByte();
                e.push(i),
                    t--
            }
            return StringAndByteUtil.byteToString(e)
        }
    }),


    /**
     * 解析AIS轨迹点数据
     * @param data
     * @return
     */
    function analyseAisTrack(data) {
        var data = decode64(data);
        var aisTrackData = new Array(); //解析数据
        var trackBytes = new a3d.ByteArray(data, a3d.Endian.LITTLE);

        var status = trackBytes.readUInt16LE(); //数据包类型		整数(uint16)	2
        aisTrackData.status = status;

        aisTrackData.data = new Array();
        if (status == 0)//成功，有数据
        {
            dataLength = trackBytes.readInt32LE(); //轨迹点长度 整数(uint32)	4
            for (var i = 0; i < dataLength; i++) {
                var dataObj = {}; //轨迹点数据
                dataObj.utc = trackBytes.readInt32LE(); //航点时间	整数(int32)	4
                dataObj.lon = trackBytes.readInt32LE(); //百万分之一度，没查到则返回非法值[-90000000,9000000] 整数(int32)	4
                dataObj.lat = trackBytes.readInt32LE(); //百万分之一度，没查到则返回非法值[-180000000,18000000]	整数(int32)	4
                dataObj.sog = trackBytes.readUInt16LE(); //对地速率	,毫米/秒,65535作为非法值	整数(int16)	2   转成节
                dataObj.cog = trackBytes.readUInt16LE(); //对地航向,百分之一度[0-36000]	整数(int16)	2
                dataObj.hdg = trackBytes.readUInt16LE(); //船首向	整数（int16）	2
                dataObj.rot = trackBytes.readUInt16LE(); //旋转角速度	整数（int16）	2
                dataObj.navistatus = trackBytes.readByte(); //航行状态	整数(byte)	1
                dataObj.from = trackBytes.readByte(); //数据类型	整数(byte)	1
                aisTrackData.data.push(dataObj);
            }
            //while (trackBytes.pos < dataLength ) {}
            aisTrackData.isMoreData = trackBytes.readInt32LE(); //时间	整数(int32)	4
        }
        return aisTrackData.data;
    }